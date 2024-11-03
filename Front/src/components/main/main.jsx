import React, { useState } from 'react';
import "./style/style.css";
import Kittens from "./../../Img/kittens.svg";

function Main() {
    const [idToInput, setIdToInput] = useState('');
    const [idFromInput, setIdFromInput] = useState('');
    const [reviewInput, setReviewInput] = useState('');

    const handleIdToInput = (event) => {
        setIdToInput(event.target.value);
    };

    const handleIdFromInput = (event) => {
        setIdFromInput(event.target.value);
    };

    const handleReviewInput = (event) => {
        setReviewInput(event.target.value);
    };


    const handleSubmit = () => {
        // Обработка ввода пользователя и критериев
        // ... (ваш код для обработки данных)


    };

    return (
        <div className="app">
            <header>
                <h1 className="header-title">INNOGLOBALHACK</h1> {/* Добавлено имя */}
            </header>
            <div className="content"> {/* Добавлено для центрирования */}
                <img src={Kittens} alt="Векторное изображение" />
                <div className="form-container">
                    <form id="IdToInputForm" onSubmit={(event) => event.preventDefault()}>
                        <input
                            type="text"
                            id="inputIdTo"
                            placeholder="Введите id сотрудника"
                            value={idToInput}
                            onChange={handleIdToInput}
                        />
                    </form>

                    <form id="IdFromInputForm" onSubmit={(event) => event.preventDefault()}>
                        <textarea
                            id="inputIdFrom"
                            placeholder="Введите id написавшего отзыв"
                            value={idFromInput}
                            onChange={handleIdFromInput}
                        />
                    </form>
                    <form id="ReviewInputForm" onSubmit={(event) => event.preventDefault()}>
                        <input
                            type="text"
                            id="inputReviewForm"
                            placeholder="Введите отзыв"
                            value={reviewInput}
                            onChange={handleReviewInput}
                        />
                    </form>
                </div>

                <button id="submitButton" onClick={handleSubmit}>
                    Отправить
                </button>
            </div>
            
            <div className="diamonds"> {/* Контейнер для ромбиков */}
                <div className="diamond" style={{ top: '5%', left: '5%', width: '20px', height: '20px' }}></div>
                <div className="diamond" style={{ top: '15%', left: '10%', width: '15px', height: '15px' }}></div>
                <div className="diamond" style={{ top: '25%', left: '5%', width: '25px', height: '25px' }}></div>
                <div className="diamond" style={{ top: '35%', left: '15%', width: '10px', height: '10px' }}></div>
                <div className="diamond" style={{ top: '45%', left: '5%', width: '30px', height: '30px' }}></div>
                <div className="diamond" style={{ top: '55%', left: '10%', width: '20px', height: '20px' }}></div>
                <div className="diamond" style={{ top: '65%', left: '5%', width: '15px', height: '15px' }}></div>
                <div className="diamond" style={{ top: '75%', left: '10%', width: '25px', height: '25px' }}></div>
                <div className="diamond" style={{ top: '85%', left: '15%', width: '10px', height: '10px' }}></div>
                <div className="diamond" style={{ top: '95%', left: '5%', width: '30px', height: '30px' }}></div>
                <div className="diamond" style={{ top: '5%', left: '5%', width: '20px', height: '20px' }}></div>
                <div className="diamond" style={{ top: '15%', left: '15%', width: '15px', height: '15px' }}></div>
                <div className="diamond" style={{ top: '25%', left: '10%', width: '25px', height: '25px' }}></div>
                <div className="diamond" style={{ top: '35%', left: '5%', width: '10px', height: '10px' }}></div>
                <div className="diamond" style={{ top: '45%', left: '10%', width: '30px', height: '30px' }}></div>
                <div className="diamond" style={{ top: '55%', left: '5%', width: '20px', height: '20px' }}></div>
                <div className="diamond" style={{ top: '65%', left: '10%', width: '15px', height: '15px' }}></div>
                <div className="diamond" style={{ top: '75%', left: '5%', width: '25px', height: '25px' }}></div>
                <div className="diamond" style={{ top: '85%', left: '10%', width: '10px', height: '10px' }}></div>
                <div className="diamond" style={{ top: '95%', left: '5%', width: '30px', height: '30px' }}></div>
                <div className="diamond" style={{ top: '10%', left: '20%', width: '18px', height: '18px' }}></div>
                <div className="diamond" style={{ top: '20%', left: '25%', width: '22px', height: '22px' }}></div>
                <div className="diamond" style={{ top: '30%', left: '15%', width: '12px', height: '12px' }}></div>
                <div className="diamond" style={{ top: '40%', left: '25%', width: '28px', height: '28px' }}></div>
                <div className="diamond" style={{ top: '50%', left: '20%', width: '16px', height: '16px' }}></div>

            </div>
        </div>
    );
}

export default Main;
