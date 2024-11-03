import { Route, Routes, useLocation } from "react-router-dom";
import Reviews from "./components/reviews/reviews.jsx"; 
//import Main from "./components/main/main.jsx"; 


import "./components/reviews/style/style.css";
//import "./components/main/style/style.css";

function App() {
  return (
    <>
      <Routes>
        <Route path="/" element={<Reviews />} />
      </Routes>
    </>
  );
}

export default App;

//<Route path="/main" element={<Main />} />