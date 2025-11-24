import React, { useState } from 'react';
import QuestionScreen from './components/QuestionScreen';
import ResultScreen from './components/ResultScreen';
import HistoryScreen from './components/HistoryScreen';
import './styles/main.css';

const QUESTIONS = [
  { id: 1, text: "歩行は一人でできますか？", yesValue: 0, noValue: 1 }, // Yes=Good(0), No=Bad(1)
  { id: 2, text: "食事は自分で摂れますか？", yesValue: 0, noValue: 1 },
  { id: 3, text: "入浴は一人でできますか？", yesValue: 0, noValue: 1 },
  { id: 4, text: "排泄は自分でできますか？", yesValue: 0, noValue: 1 },
  { id: 5, text: "記憶や判断に不安を感じますか？", yesValue: 1, noValue: 0 }, // Yes=Bad(1), No=Good(0)
];

function App() {
  const [step, setStep] = useState(0); // 0=Start, 1-5=Questions, 6=Result, 7=History
  const [answers, setAnswers] = useState([]);
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleStart = () => {
    setStep(1);
    setAnswers([]);
    setResult(null);
  };

  const handleAnswer = async (value) => {
    const newAnswers = [...answers, { question_id: QUESTIONS[step - 1].id, answer_value: value }];
    setAnswers(newAnswers);

    if (step < QUESTIONS.length) {
      setStep(step + 1);
    } else {
      // Submit answers
      setLoading(true);
      try {
        const response = await fetch('/api/assess', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({ answers: newAnswers }),
        });
        const data = await response.json();
        setResult(data);
        setStep(6);
      } catch (error) {
        console.error("Error submitting assessment:", error);
        alert("エラーが発生しました。もう一度お試しください。");
        setStep(0);
      } finally {
        setLoading(false);
      }
    }
  };

  if (step === 0) {
    return (
      <div className="container" style={{ textAlign: 'center', paddingTop: '100px' }}>
        <h1>シニアナビ<br />簡易介護チェック</h1>
        <p style={{ fontSize: '24px', marginBottom: '50px' }}>
          簡単な質問に答えるだけで、<br />
          今の状態をチェックできます。
        </p>
        <button className="btn-primary btn-large" onClick={handleStart}>
          チェックを始める
        </button>
        <button className="btn-secondary" onClick={() => setStep(7)} style={{ marginTop: '20px' }}>
          履歴を見る
        </button>
      </div>
    );
  }

  if (loading) {
    return (
      <div className="container" style={{ textAlign: 'center', paddingTop: '100px' }}>
        <h2>判定中...</h2>
      </div>
    );
  }

  if (step === 6 && result) {
    return <ResultScreen result={result} onRestart={handleStart} />;
  }

  if (step === 7) {
    return <HistoryScreen onBack={() => setStep(0)} />;
  }

  return (
    <QuestionScreen
      question={QUESTIONS[step - 1]}
      onAnswer={handleAnswer}
      currentStep={step}
      totalSteps={QUESTIONS.length}
    />
  );
}

export default App;
