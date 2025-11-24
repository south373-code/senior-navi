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
                <button className="btn-secondary" onClick={() => alert('実際のアプリでは電話発信や地図が開きます')}>
                    地域包括支援センターに電話
                </button>
                <button className="btn-secondary" onClick={() => alert('実際のアプリでは医療機関検索が開きます')}>
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
