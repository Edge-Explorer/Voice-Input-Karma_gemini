import React, { useState } from 'react';
import { StyleSheet, View, TextInput, Button, Text, ActivityIndicator, Alert } from 'react-native';

const QAScreen = () => {
  const [question, setQuestion] = useState('');
  const [answer, setAnswer] = useState('');
  const [loading, setLoading] = useState(false);

  // Replace this with your actual server address
  // For local development with Metro on Android, use 10.0.2.2 instead of localhost
  // For iOS simulator, you can use localhost
  // For a physical device, use your computer's IP address on the local network
  const SERVER_URL = 'http://10.0.2.2:5000'; // Change as needed for your environment

  const handleSubmit = async () => {
    if (!question.trim()) {
      Alert.alert('Error', 'Please enter a question');
      return;
    }
    
    setLoading(true);
    
    try {
      const response = await fetch(`${SERVER_URL}/api/question`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ question }),
      });
      
      if (!response.ok) {
        throw new Error('Server responded with an error');
      }
      
      const data = await response.json();
      
      if (data && data.answer) {
        setAnswer(data.answer);
      } else {
        setAnswer('Sorry, could not get an answer.');
      }
    } catch (error) {
      console.error('Error submitting question:', error);
      setAnswer('Error connecting to server. Please try again.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Q&A Application</Text>
      
      <TextInput
        style={styles.input}
        placeholder="Enter your question here"
        value={question}
        onChangeText={setQuestion}
        multiline
      />
      
      <Button
        title={loading ? "Loading..." : "Submit Question"}
        onPress={handleSubmit}
        disabled={loading || !question.trim()}
      />
      
      {loading && <ActivityIndicator style={styles.loader} />}
      
      <Text style={styles.answerLabel}>Answer:</Text>
      <TextInput
        style={styles.answerBox}
        value={answer}
        editable={false}
        multiline
        placeholder="The answer will appear here"
      />
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    padding: 20,
    backgroundColor: '#fff',
  },
  title: {
    fontSize: 24,
    fontWeight: 'bold',
    marginBottom: 20,
    textAlign: 'center',
  },
  input: {
    borderWidth: 1,
    borderColor: '#ddd',
    borderRadius: 5,
    padding: 10,
    marginBottom: 20,
    minHeight: 80,
  },
  loader: {
    marginVertical: 10,
  },
  answerLabel: {
    fontSize: 18,
    fontWeight: 'bold',
    marginTop: 20,
    marginBottom: 10,
  },
  answerBox: {
    borderWidth: 1,
    borderColor: '#ddd',
    borderRadius: 5,
    padding: 10,
    minHeight: 120,
    backgroundColor: '#f9f9f9',
  },
});

export default QAScreen;