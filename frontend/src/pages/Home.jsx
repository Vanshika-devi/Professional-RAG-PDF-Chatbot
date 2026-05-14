import Navbar from "../components/Navbar";

import UploadBox from "../components/UploadBox";

import ChatWindow from "../components/ChatWindow";

function Home() {

  return (
    <div>

      <Navbar />

      <div className="container">

        <UploadBox />

        <ChatWindow />

      </div>

    </div>
  );
}

export default Home;