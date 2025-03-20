import Chatbot from "@/components/Chatbot";
import logo from "@/assets/images/logo.png";
import background from "@/assets/images/background.png";
import bird from "@/assets/images/bird.png";

function App() {
  return (
    <div className="relative min-h-screen w-full">
      <div
        style={{
          backgroundImage: `url(${background})`,
          backgroundSize: "cover",
          backgroundPosition: "center",
          backgroundAttachment: "fixed",
        }}
        className="absolute inset-0 -z-10"
      ></div>
      <div className="flex flex-col min-h-screen w-full max-w-3xl mx-auto px-4 bg-white bg-opacity-70 backdrop-blur-md relative z-10 rounded-lg">
        <header className="sticky top-0 shrink-0 z-20">
          <div className="flex items-center justify-between h-full w-full pt-4 pb-2 bg-white bg-opacity-70 backdrop-blur-md relative z-10 rounded-lg">
            <img src={logo} className="w-32" alt="logo" />
            <h1 className="font-urbanist text-[1.65rem] font-semibold text-center flex-grow">
              WildGPT
            </h1>
            <img src={bird} className="w-32" alt="logo" />
          </div>
        </header>
        <Chatbot />
      </div>
    </div>
  );
}

export default App;
