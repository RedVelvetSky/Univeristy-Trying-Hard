using System;
using System.Collections.Generic;
using System.Linq;

namespace WordCounting
{
    class ReadInput
    {
        public static string ReadSingleWord(){

            char character  = (char)Console.Read();
            string word = "";

            while (!char.IsLetter(character)) 
            {
                // the first character is read and checked for being a letter outside the loop
                character = (char)Console.Read();
            }

            while (char.IsLetter(character))
            {
                // then the loop is entered to read and concatenate the rest of the letters
                word += character;
                character = (char)Console.Read();
            }

            return word;
            
        }
    }

    class MainClass
    {
        static void Main(string[] args){

            // reding first endword
            string EndingWord = ReadInput.ReadSingleWord();

            // rading first non-endword word
            string RegularWord = ReadInput.ReadSingleWord();

            // initializing a dictionary by declaring it with the Dictionary<TKey, TValue> class and then instantiating it using the new keyword
            Dictionary<string, int> WordCount = new Dictionary<string, int>();

            // reading sequantually only words and adding them to dictionary. Stop when reach endword again
            while (RegularWord != EndingWord)
            {
                if (WordCount.ContainsKey(RegularWord)){
                    WordCount[RegularWord]++;
                } else {
                    WordCount[RegularWord] = 1;
                }

                RegularWord = ReadInput.ReadSingleWord();
            }

            // sorting our dictionary by value in descending order and then use the Take method to get the top 20 entries
            var TopWords = WordCount.OrderByDescending(pair => pair.Value).Take(20);

            // printing the word frequancies
            foreach (KeyValuePair<string, int> pair in TopWords)
            {
                Console.WriteLine("{0} {1}", pair.Key, pair.Value);
            }

        }
    }
}