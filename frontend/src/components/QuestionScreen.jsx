import React from 'react';

const QuestionScreen = ({ question, onAnswer, currentStep, totalSteps }) => {
    return (
        <div className="container">
            <div style={{ textAlign: 'center', marginBottom: '20px', fontSize: '18px' }}>
                質問 {currentStep} / {totalSteps}
            </div>
            <h2 className="question-text">{question.text}</h2>

            <div style={{ marginTop: '50px' }}>
                <button
                    className="btn-primary btn-large"
                    onClick={() => onAnswer(question.yesValue)}
                >
                    はい
                </button>
                <button
                    className="btn-secondary btn-large"
                    onClick={() => onAnswer(question.noValue)}
                >
                    いいえ
                </button>
            </div>
        </div>
    );
};

export default QuestionScreen;
