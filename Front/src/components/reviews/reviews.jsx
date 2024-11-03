import React, { useState } from 'react';
import "./style/style.css";
import Kittens from "./../../Img/kittens.svg"; 

function Reviews() {
    const [userInput, setUserInput] = useState('');
    const [criteriaInput, setCriteriaInput] = useState('');
    const [useDefaultData, setUseDefaultData] = useState(false);
    const [output, setOutput] = useState('');

    const handleUserInput = (event) => {
        setUserInput(event.target.value);
    };

    const handleCriteriaInput = (event) => {
        setCriteriaInput(event.target.value);
    };

    const toggleInput = () => {
        setUseDefaultData(!useDefaultData);
        if (useDefaultData) {
            setCriteriaInput('');
        } else {
            setCriteriaInput('');
        }
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
                    <form id="userInputForm" onSubmit={(event) => event.preventDefault()}>
                        <input
                            type="text"
                            id="inputUser"
                            placeholder="Введите имя пользователя"
                            value={userInput}
                            onChange={handleUserInput}
                        />
                    </form>

                    <form id="criteriaForm" onSubmit={(event) => event.preventDefault()}>
                        <textarea
                            id="inputCriteria"
                            placeholder="Введите критерии"
                            value={criteriaInput}
                            onChange={handleCriteriaInput}
                        />
                        <label>
                            <input
                                type="checkbox"
                                id="defaultCheckbox"
                                className="checkbox-style"
                                checked={useDefaultData}
                                onChange={toggleInput}
                            />
                            Использовать данные по умолчанию
                        </label>
                    </form>
                </div>

                <button id="submitButton" onClick={handleSubmit}>
                    Отправить
                </button>

                <div className="output">{output}</div>
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

export default Reviews;