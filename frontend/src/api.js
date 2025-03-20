const BASE_URL = import.meta.env.VITE_API_URL;

async function createChat() {
  const res = await fetch("http://localhost:8000" + "/chats", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
  });
  const data = await res.json();
  if (!res.ok) {
    return Promise.reject({ status: res.status, data });
  }
  return data;
}

async function sendChatMessage(chatId, message) {
  const res = await fetch("http://localhost:8000" + `/chat`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ message }),
  });
  console.log(res);
  if (!res.ok) {
    return Promise.reject({ status: res.status, data: await res.json() });
  }
  return res.json();
}

export default {
  sendChatMessage,
};
