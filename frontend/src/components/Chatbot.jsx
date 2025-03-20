import { useState } from "react";
import { useImmer } from "use-immer";
import api from "@/api";
import { parseSSEStream } from "@/utils";
import ChatMessages from "@/components/ChatMessages";
import ChatInput from "@/components/ChatInput";
function Chatbot() {
  const [chatId, setChatId] = useState(null);
  const [messages, setMessages] = useState([]);
  const [newMessage, setNewMessage] = useState("");

  const isLoading = messages.length && messages[messages.length - 1].loading;

  async function submitNewMessage() {
    const trimmedMessage = newMessage.trim();
    if (!trimmedMessage || isLoading) return;

    let temp = [
      ...messages,
      { role: "user", content: trimmedMessage },
      { role: "assistant", content: "", sources: [], loading: true },
    ]

    setMessages(temp);
    setNewMessage("");

    let chatIdOrNew = chatId;
    try {
      if (!chatId) {
        const { id } = "await api.createChat()";
        setChatId(id);
        chatIdOrNew = id;
      }

      const stream = await api.sendChatMessage(chatIdOrNew, trimmedMessage);
      temp[temp.length-1].content = stream.response
      temp[temp.length-1].loading = false
      setMessages(temp)
    } catch (err) {
      console.log(err);
      let temp = messages;
      temp[temp.length-1]['error'] = true
      temp[temp.length-1].loading = false
      setMessages(temp);
    }
  }

  return (
    <div className="relative grow flex flex-col gap-6 pt-6">
      {messages.length === 0 && (
        <div className="mt-3 font-urbanist text-primary-blue text-xl font-light space-y-2">
          <p>👋 Welcome!</p>
          <p>
            Hey there !! I'm WildGPT, an AI-powered tool designed to scrape and 
            consolidate publicly available research papers and data related to wildlife, biodiversity, and conservation.
          </p>
          <p>Ask me anything about the latest research trends.</p>
        </div>
      )}
      <ChatMessages messages={messages} isLoading={isLoading} />
      <ChatInput
        newMessage={newMessage}
        isLoading={isLoading}
        setNewMessage={setNewMessage}
        submitNewMessage={submitNewMessage}
      />
    </div>
  );
}

export default Chatbot;
