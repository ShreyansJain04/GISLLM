import React from "react";
import { motion } from "framer-motion";
import ReactMarkdown from "react-markdown";
import { ArrowRightIcon, CheckCircleIcon, XCircleIcon } from "@heroicons/react/24/outline";

const MessageBubble = ({
  message,
  isUser,
  citations,
  timestamp,
  showContinueButton,
  onContinue,
  continueClicked,
  children,
  showOptions,
  options,
  onOptionSelect,
  selectedOptionIndex,
  feedback,
  isCorrect,
  correctAnswer,
  submitted = false,
  mode = "default",
}) => {

  const getOptionStyle = (index) => {
    const baseStyle = "w-full text-left px-3 py-2 border rounded-lg transition-all duration-200 text-sm";
    
    if (!submitted) {
      // Before submission
      if (selectedOptionIndex === index.toString() || selectedOptionIndex === index) {
        return `${baseStyle} bg-primary-100 border-primary-500 text-primary-700 ring-2 ring-primary-200`;
      }
      return `${baseStyle} bg-secondary-50 hover:bg-secondary-100 border-secondary-200 hover:border-secondary-300`;
    } else {
      // After submission - show correct/incorrect
      if ((selectedOptionIndex === index.toString() || selectedOptionIndex === index)) {
        if (isCorrect) {
          return `${baseStyle} bg-green-100 border-green-500 text-green-700 ring-2 ring-green-200`;
        } else {
          return `${baseStyle} bg-red-100 border-red-500 text-red-700 ring-2 ring-red-200`;
        }
      } else if (correctAnswer !== undefined && index === correctAnswer) {
        // Show correct answer if available
        return `${baseStyle} bg-green-50 border-green-400 text-green-600 ring-1 ring-green-100`;
      }
      return `${baseStyle} bg-secondary-25 border-secondary-200 text-secondary-500`;
    }
  };

  return (
    <motion.div
      initial={{ opacity: 0, y: 10 }}
      animate={{ opacity: 1, y: 0 }}
      className={`flex ${isUser ? "justify-end" : "justify-start"} mb-4`}
    >
      <div className={`max-w-3xl ${isUser ? "order-2" : "order-1"}`}>
        <div
          className={`px-4 py-3 rounded-2xl ${
            isUser
              ? "bg-primary-600 text-white rounded-br-sm"
              : "bg-white border border-secondary-200 text-secondary-900 rounded-bl-sm"
          }`}
        >
          <div className="prose prose-sm max-w-none">
            {isUser ? (
              <p className="text-white mb-0">{message}</p>
            ) : (
              <ReactMarkdown
                components={{
                  p: ({ children }) => (
                    <p className="mb-2 last:mb-0">{children}</p>
                  ),
                  ul: ({ children }) => <ul className="ml-4 mb-2">{children}</ul>,
                  ol: ({ children }) => <ol className="ml-4 mb-2">{children}</ol>,
                  li: ({ children }) => <li className="mb-1">{children}</li>,
                  code: ({ children }) => (
                    <code className="bg-secondary-100 px-1 py-0.5 rounded text-xs">
                      {children}
                    </code>
                  ),
                }}
              >
                {message}
              </ReactMarkdown>
            )}
          </div>
          
          {/* Citations */}
          {citations && citations.length > 0 && (
            <div className="mt-3 pt-2 border-t border-secondary-200">
              <p className="text-xs text-secondary-500 mb-1">Sources:</p>
              <div className="space-y-1">
                {citations.map((citation, index) => {
                  const isUrl =
                    typeof citation === "string" &&
                    (citation.startsWith("http://") ||
                      citation.startsWith("https://"));
                  return (
                    <div
                      key={index}
                      className="text-xs bg-secondary-50 px-2 py-1 rounded"
                    >
                      <span className="mr-1">📄</span>
                      {isUrl ? (
                        <a
                          href={citation}
                          target="_blank"
                          rel="noopener noreferrer"
                          className="text-primary-700 underline hover:text-primary-900"
                        >
                          {citation}
                        </a>
                      ) : (
                        <span className="text-primary-700 underline hover:text-primary-900 cursor-pointer">
                          {citation}
                        </span>
                      )}
                    </div>
                  );
                })}
              </div>
            </div>
          )}

          {/* Feedback Display */}
          {feedback && submitted && !isUser && (
            <div className="mt-3 pt-2 border-t border-secondary-200">
              <div className={`p-3 rounded-lg ${
                isCorrect
                  ? "bg-green-50 border border-green-200"
                  : "bg-red-50 border border-red-200"
              }`}>
                <div className="flex items-start space-x-2">
                  {isCorrect ? (
                    <CheckCircleIcon className="w-5 h-5 text-green-500 flex-shrink-0" />
                  ) : (
                    <XCircleIcon className="w-5 h-5 text-red-500 flex-shrink-0" />
                  )}
                  <div className="prose prose-sm max-w-none">
                    <ReactMarkdown>
                      {typeof feedback === "string" ? feedback : JSON.stringify(feedback)}
                    </ReactMarkdown>
                  </div>
                </div>
              </div>
            </div>
          )}
          
          {/* Continue Button (optional) */}
          {showContinueButton && !isUser && !continueClicked && (
            <div className="mt-3 pt-2 border-t border-secondary-200">
              <button
                onClick={onContinue}
                className="flex items-center space-x-2 px-3 py-2 bg-primary-600 hover:bg-primary-700 text-white text-sm rounded-lg transition-colors duration-200"
              >
                <span>Continue</span>
                <ArrowRightIcon className="w-4 h-4" />
              </button>
            </div>
          )}
          
          {/* Multiple Choice Options */}
          {showOptions && options && options.length > 0 && !isUser && (
            <div className="mt-3 pt-2 border-t border-secondary-200">
              <p className="text-xs text-secondary-500 mb-2">
                {mode === "learn" ? "GeoTutor Question - Select an answer:" : "Select an answer:"}
              </p>
              <div className="space-y-2">
                {options.map((option, index) => (
                  <button
                    key={index}
                    onClick={() => !submitted && onOptionSelect(index)}
                    className={getOptionStyle(index)}
                    disabled={submitted}
                  >
                    <div className="flex items-center justify-between">
                      <div className="flex items-center">
                        <span className="font-medium text-secondary-700 mr-2">
                          {String.fromCharCode(65 + index)}.
                        </span>
                        <span>{option}</span>
                      </div>
                      {submitted && (selectedOptionIndex === index.toString() || selectedOptionIndex === index) && (
                        <span className="ml-2">
                          {isCorrect ? (
                            <CheckCircleIcon className="w-4 h-4 text-green-500" />
                          ) : (
                            <XCircleIcon className="w-4 h-4 text-red-500" />
                          )}
                        </span>
                      )}
                      {submitted && correctAnswer !== undefined && index === correctAnswer && (selectedOptionIndex !== index.toString() && selectedOptionIndex !== index) && (
                        <span className="ml-2">
                          <CheckCircleIcon className="w-4 h-4 text-green-400" />
                        </span>
                      )}
                    </div>
                  </button>
                ))}
              </div>
            </div>
          )}
          {children}
        </div>
        <div
          className={`text-xs text-secondary-500 mt-1 ${
            isUser ? "text-right" : "text-left"
          }`}
        >
          {timestamp && new Date(timestamp).toLocaleTimeString()}
        </div>
      </div>
    </motion.div>
  );
};

export default MessageBubble;
