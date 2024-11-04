import React from "react"; //импортируем библиотеку react
import ReactDOM from "react-dom/client"; //библиотеку для работы с dom
import { BrowserRouter } from "react-router-dom";
import App from "./App"; //приложение
import { Toaster } from "react-hot-toast";
//находим элемент root и создаем экземпляр dom
const root = ReactDOM.createRoot(document.getElementById("root"));
//вызываем функцию render и передаем наше приложение
root.render(
  <React.StrictMode>
    <BrowserRouter>
      <Toaster />
      <App />
    </BrowserRouter>
  </React.StrictMode>
);
