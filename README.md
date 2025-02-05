# Hotel Reviews Sentiment Analysis using MapReduce

## 📌 Project Background
Analyzing customer reviews is crucial in the hospitality industry to understand user sentiments and improve services. This project implements a MapReduce framework from scratch to process hotel reviews, categorize them as positive, negative, or neutral, and identify the most popular and most criticized hotels.

## 📝 Introduction
This project applies the MapReduce paradigm to sentiment analysis of hotel reviews. The dataset contains customer reviews of hotels, and the system processes these reviews to classify sentiments based on predefined positive, negative, and neutral keywords. The MapReduce framework is manually implemented using Python functions to map, shuffle, sort, and reduce data, showcasing how large-scale data processing can be structured.

## 🛠 Tools & Technologies Used
- **Python**: Core programming language used for implementation
- **Pandas**: Used for data preprocessing and handling tabular data efficiently
- **NumPy**: Used for efficient numerical operations

## 📂 Project Structure
- **Dataset Loading & Preprocessing**: The dataset is cleaned by removing missing values and duplicates.
- **Mapper Function**: Processes each review and assigns a sentiment category.
- **Shuffle & Sort**: Organizes mapped data by hotel names.
- **Reducer Function**: Aggregates sentiment counts for each hotel.
- **Analysis & Output**: Displays overall sentiment distribution and top 10 most loved and hated hotels.

## 🏆 What I Learned
- Understanding the fundamentals of MapReduce and its practical implementation
- How to manually implement distributed computing concepts using Python
- Importance of data preprocessing in sentiment analysis
- Efficient sorting and aggregation techniques in Python
- How keyword-based sentiment classification works

## 📌 Conclusion
This project demonstrates how MapReduce principles can be applied to process large-scale text data efficiently. While this implementation is done on a single machine, the same logic can be extended to distributed computing frameworks like Hadoop or Spark for big data analysis.

## 🚀 Future Enhancements
- Extending the implementation to a distributed framework like Hadoop or Spark
- Using Natural Language Processing (NLP) techniques for better sentiment classification
- Implementing sentiment weighting instead of simple word matching
- Expanding the keyword list for multilingual sentiment detection
