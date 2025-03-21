import { useState } from "react";
import api from "@/api";
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

    // Create a new message array without mutating the original
    const newMessages = [
      ...messages,
      { role: "user", content: trimmedMessage },
      { role: "assistant", content: "", sources: [], loading: true },
    ];

    setMessages(newMessages); // Set new messages array
    setNewMessage(""); // Reset the input message

    let chatIdOrNew = chatId;
    try {
      if (!chatId) {
        const { id } = "await api.createChat()";
        setChatId(id);
        chatIdOrNew = id;
      }

      const stream = await api.sendChatMessage(chatIdOrNew, trimmedMessage);
      
      // Create a copy of the last message and update its content
      const updatedMessages = [...newMessages];
      updatedMessages[updatedMessages.length - 1] = {
        ...updatedMessages[updatedMessages.length - 1],
        content: stream.response,
        loading: false,
      };

      setMessages(updatedMessages); // Update messages state

    } catch (err) {
      console.log(err);
      const updatedMessages = [...newMessages];
      updatedMessages[updatedMessages.length - 1] = {
        ...updatedMessages[updatedMessages.length - 1],
        error: true,
        loading: false,
      };

      setMessages(updatedMessages); // Update messages state with error
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