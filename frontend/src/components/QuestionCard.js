import React, { useState, useEffect } from "react";
import { motion, AnimatePresence } from "framer-motion";
import {
  CheckCircleIcon,
  XCircleIcon,
  LightBulbIcon,
  QuestionMarkCircleIcon,
  ArrowRightIcon,
} from "@heroicons/react/24/outline";
import ReactMarkdown from "react-markdown";

const QuestionCard = ({ 
  question, 
  onAnswer, 
  loading, 
  feedback, 
  isCorrect,
  showContinueButton = false,
  onContinue = null,
  mode = "default" // "test", "learn", "review", "chat"
}) => {
  // Support both {question: {...}} and flat or string
  const q = question?.question || question;
  const qText = q?.text || (typeof q === "string" ? q : "");
  const qType = q?.type || "";
  const qOptions = q?.options || [];
  const qExplanation = q?.explanation || "";
  const correctAnswer = q?.correct_answer;

  const [answer, setAnswer] = useState("");
  const [selectedOption, setSelectedOption] = useState(null);
  const [submitted, setSubmitted] = useState(false);

  // Reset state when question changes
  useEffect(() => {
    setAnswer("");
    setSelectedOption(null);
    setSubmitted(false);
  }, [question]);

  const handleSubmit = (e) => {
    e.preventDefault();
    if (qType === "objective" && selectedOption === null) return;
    if (qType !== "objective" && !answer.trim()) return;
    setSubmitted(true);
    if (qType === "objective") {
      onAnswer(selectedOption);
    } else {
      onAnswer(answer);
    }
  };

  const getOptionStyle = (index) => {
    const baseStyle = "w-full text-left p-3 rounded-lg border transition-all duration-200";
    
    if (!submitted) {
      // Before submission
      if (selectedOption === index) {
        return `${baseStyle} border-primary-500 bg-primary-50 text-primary-700 ring-2 ring-primary-200`;
      }
      return `${baseStyle} border-secondary-200 hover:bg-secondary-50 hover:border-secondary-300`;
    } else {
      // After submission - show correct/incorrect
      if (selectedOption === index) {
        if (isCorrect) {
          return `${baseStyle} border-green-500 bg-green-50 text-green-700 ring-2 ring-green-200`;
        } else {
          return `${baseStyle} border-red-500 bg-red-50 text-red-700 ring-2 ring-red-200`;
        }
      } else if (correctAnswer !== undefined && index === correctAnswer) {
        // Show correct answer if available
        return `${baseStyle} border-green-400 bg-green-25 text-green-600 ring-1 ring-green-100`;
      }
      return `${baseStyle} border-secondary-200 bg-secondary-25 text-secondary-500`;
    }
  };

  return (
    <motion.div
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      className="bg-white rounded-xl shadow-sm border border-secondary-200 p-6"
    >
      <div className="space-y-4">
        <div className="flex items-center space-x-2">
          <LightBulbIcon className="w-5 h-5 text-yellow-500" />
          <h3 className="text-lg font-medium text-secondary-900">
            {mode === "test" ? "GeoTutor Test Question" : "Question"}
          </h3>
        </div>
        <div className="prose prose-sm max-w-none">
          <ReactMarkdown>{qText}</ReactMarkdown>
        </div>
        
        {!showContinueButton || !feedback ? (
          <form onSubmit={handleSubmit} className="space-y-4">
            {qType === "objective" &&
            Array.isArray(qOptions) &&
            qOptions.length > 0 ? (
              <div className="space-y-2">
                {qOptions.map((option, index) => (
                  <button
                    key={index}
                    type="button"
                    onClick={() => !submitted && setSelectedOption(index)}
                    className={getOptionStyle(index)}
                    disabled={loading || submitted}
                  >
                    <div className="flex items-center justify-between">
                      <span>{option}</span>
                      {submitted && selectedOption === index && (
                        <span className="ml-2">
                          {isCorrect ? (
                            <CheckCircleIcon className="w-5 h-5 text-green-500" />
                          ) : (
                            <XCircleIcon className="w-5 h-5 text-red-500" />
                          )}
                        </span>
                      )}
                      {submitted && correctAnswer !== undefined && index === correctAnswer && selectedOption !== index && (
                        <span className="ml-2">
                          <CheckCircleIcon className="w-5 h-5 text-green-400" />
                        </span>
                      )}
                    </div>
                  </button>
                ))}
              </div>
            ) : (
              <textarea
                value={answer}
                onChange={(e) => setAnswer(e.target.value)}
                placeholder="Type your answer here..."
                className="w-full h-32 p-3 rounded-lg border border-secondary-200 focus:ring-2 focus:ring-primary-500 focus:border-transparent"
                disabled={loading || feedback}
              />
            )}
            {!submitted && (
              <button
                type="submit"
                disabled={
                  loading ||
                  (qType === "objective" ? selectedOption === null : !answer.trim())
                }
                className="w-full py-2 px-4 bg-primary-600 text-white rounded-lg hover:bg-primary-700 disabled:opacity-50 transition-colors duration-200"
              >
                {loading ? "Checking..." : "Submit Answer"}
              </button>
            )}
          </form>
        ) : null}

        <AnimatePresence>
          {feedback && (
            <motion.div
              initial={{ opacity: 0, y: -10 }}
              animate={{ opacity: 1, y: 0 }}
              exit={{ opacity: 0, y: -10 }}
              className={`p-4 rounded-lg ${
                isCorrect
                  ? "bg-green-50 border border-green-200"
                  : "bg-red-50 border border-red-200"
              }`}
            >
              <div className="flex items-start space-x-2">
                {isCorrect ? (
                  <CheckCircleIcon className="w-5 h-5 text-green-500 flex-shrink-0" />
                ) : (
                  <XCircleIcon className="w-5 h-5 text-red-500 flex-shrink-0" />
                )}
                <div className="prose prose-sm max-w-none">
                  <ReactMarkdown>
                    {typeof feedback === "string"
                      ? feedback
                      : JSON.stringify(feedback)}
                  </ReactMarkdown>
                </div>
              </div>
            </motion.div>
          )}
        </AnimatePresence>

        {qType === "objective" && feedback && qExplanation && (
          <div className="mt-3 p-3 rounded bg-blue-50 border border-blue-200">
            <div className="flex items-center space-x-2 mb-2">
              <QuestionMarkCircleIcon className="w-4 h-4 text-blue-500" />
              <strong className="text-blue-900">Explanation:</strong>
            </div>
            <div className="prose prose-sm max-w-none">
              <ReactMarkdown>{qExplanation}</ReactMarkdown>
            </div>
          </div>
        )}

        {showContinueButton && feedback && onContinue && (
          <motion.button
            initial={{ opacity: 0, y: 10 }}
            animate={{ opacity: 1, y: 0 }}
            onClick={onContinue}
            className="w-full py-3 px-4 bg-primary-600 text-white rounded-lg hover:bg-primary-700 transition-colors duration-200 flex items-center justify-center space-x-2"
          >
            <span>Continue</span>
            <ArrowRightIcon className="w-4 h-4" />
          </motion.button>
        )}
      </div>
    </motion.div>
  );
};

export default QuestionCard;
