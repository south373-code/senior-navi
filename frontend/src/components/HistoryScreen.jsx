import React, { useEffect, useState } from 'react';

const HistoryScreen = ({ onBack }) => {
    const [history, setHistory] = useState([]);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        fetch('http://localhost:8000/api/history')
            .then(res => res.json())
            .then(data => {
                setHistory(data);
                setLoading(false);
            })
            .catch(err => {
                console.error(err);
                setLoading(false);
            });
    }, []);

    return (
        <div className="container">
            <h1>履歴</h1>
            <button className="btn-secondary" onClick={onBack} style={{ marginBottom: '20px' }}>
                戻る
            </button>

            {loading ? (
                <p>読み込み中...</p>
            ) : (
                <div>
                    {history.length === 0 ? (
                        <p>履歴はありません。</p>
                    ) : (
                        history.map((item) => (
                            <div key={item.id} style={{ border: '1px solid #ccc', padding: '15px', marginBottom: '10px', borderRadius: '8px' }}>
                                <div style={{ fontSize: '18px', fontWeight: 'bold' }}>{item.date}</div>
                                <div style={{ fontSize: '20px', color: item.level.includes('自立') ? 'green' : item.level.includes('要支援') ? '#856404' : 'red' }}>
                                    {item.level}
                                </div>
                                <div>スコア: {item.score}</div>
                            </div>
                        ))
                    )}
                </div>
            )}
        </div>
    );
};

export default HistoryScreen;
