## UNIT TESTING Explanation

Unit Testing Framework: Pytest for Python

Test functions are made for the following predict.py functions:
1. clean_up_sentence()
2. bag_of_words()
3. predict_classes()
4. get_response()

The test function for each of the above mentioned function is preceded by "test_"

### test_clean_up_sentence()

This function accepts user input as a parameter and lemmetizes it so that the input can be understood by the chatbot.

To check if the function is working properly following three test cases are made:

(a) paramter : "My name is Lakshay"
return value : ['My', 'name', 'is', 'Lakshay']
This is a general case

(b) paramter : "How do I order?"
return value : [How','do', 'I', 'order', '?']
This case checks if '?' or any other punctuation is correctly separated

(c) paramter : "Goodbye, see you"
return value : ['Goodbye', ',', 'see', 'you']
This case checks if ',' or any other delimeter is correctly separated

### test_bag_of_words()

This function accepts user input as a parameter and returns a bag of words in the form of an array which indicates if a word is present in the list of intents or not. Presence of a word is denoted using '1' and absence using '0'. Complete length of the array is 196, which is the number of intents in the intets.json file.

To check if the function is working properly following three test casses are made:

(a) parameter : "How do I return my order"
return value : array of 0s with 1s at indexes 22, 23, 81, 131, 139, 151.

(a) parameter : "order details"
return value : array of 0s with 1s at indexes 78 and 39.

(a) parameter : "Hello"
return value : array of 0s.
This test case is for when the word is not found in the intents of words.pk1.

### test_predict_classes()

This function accepts user input as a parameter and returns the intent class along with the matching probability from the ML model. This result is in the form of a class list.

To check if the function is working properly following three test cases are made:

(a) parameter : "Refund item"
return value : [{'intent': 'returns', 'probability': '0.8146781'}]
"Refund item" is correctly predicted to be in the returns class.

(b) parameter : "Hello"
return value : [{'intent': 'greetings', 'probability': '0.68960893'}]
"Hello" is correctly predicted to be in the greetings class.

(c) parameter : "See you"
return value : [{'intent': 'goodbyes', 'probability': '0.99989593'}]
"See you" is correctly predicted to be in the goodbyes class.

Multiple test cases make sure that the intent is correctly predicted, along with correct probablity values.

### test_get_response()

This function takes a dictionary as parameter. The dictionary consists of the intent class and the probability values that are obtained from the predict_classes() function. It uses the dictionary to pick a random output message from intents.json.

To check if the function is working properly following test case are made:

(a) parameter : [{'intent': 'returns', 'probability': '0.8146781'}]
return value : randomly selected response from intents.json from the respective intent.
One example of the return value is : "How do I return an item"

