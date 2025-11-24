import React from 'react';

const ResultScreen = ({ result, onRestart }) => {
    return (
        <div className="container">
            <h1>判定結果</h1>

            <div className={`result-card result-${result.color}`}>
                <h2>{result.level}</h2>
                <p style={{ fontSize: '24px', margin: '20px 0' }}>{result.message}</p>
            </div>

            <div style={{ marginTop: '40px' }}>
                <h3>相談窓口</h3>
                <button className="btn-secondary" onClick={() => window.open('https://www.google.com/maps/search/?api=1&query=地域包括支援センター', '_blank')}>
                    近くの地域包括支援センターを探す
                </button>
                <button className="btn-secondary" onClick={() => window.open('https://www.google.com/maps/search/?api=1&query=病院', '_blank')}>
                    近くの病院を探す
                </button>
            </div>

            <div style={{ marginTop: '40px' }}>
                <button className="btn-primary" onClick={onRestart}>
                    最初に戻る
                </button>
            </div>
        </div>
    );
};

export default ResultScreen;
