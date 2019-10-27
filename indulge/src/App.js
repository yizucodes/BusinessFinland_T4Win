import React from "react";
import "./App.css";
import Header from "./components/Header";
import ImgMediaCard from "./components/Card";
import RowTransport from "./components/RowTransport";
import Clues from "./components/Clues";

function App() {
  return (
    <div className="App">
      <Header />
      {/* <ImgMediaCard /> */}
      {/* <RowTransport /> */}
      <Clues />
    </div>
  );
}

export default App;
