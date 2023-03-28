using System;
using System.IO;
using System.Text.RegularExpressions;
using System.Text;


namespace FractionalArithmetic
{
    public class Fraction
    {
        // числитель
        private int numerator = 0; 

        //  знаменатель 
        private int denominator = 0;

        public bool isWholeZero = false;

        public bool ZeroDivisionOccured = false;

        public void Exchange()
        {
            this.numerator = denominator;
            this.denominator = numerator;
        }

        public void Simplify()
        {
            int gcd = GreatestCommonDivisor(numerator, denominator);

            this.numerator /= gcd;
            this.denominator /= gcd;
            
            if (this.numerator == this.denominator)
            {
                this.numerator = 1;
                this.denominator = 1;
            }
        }

        public void SetFraction(int numerator, int denominator)
        {
            this.numerator = numerator;
            this.denominator = denominator;
        }

        public void WriteFraction()
        {
            if (denominator != 1)
            {
                if (denominator < 0)
                {
                    Console.WriteLine($"{-numerator}/{-denominator}");
                }
                else
                {
                    Console.WriteLine($"{numerator}/{denominator}");
                }
            }
            else
            {
                Console.WriteLine($"{numerator}");
            }
        }

        public void WriteFractionToLine(StringBuilder resultingStringBuilder)
        {
            if (denominator != 1)
            {
                if (denominator < 0)
                {
                    resultingStringBuilder.AppendLine ($"{-numerator}/{-denominator}");
                }
                else
                {
                  resultingStringBuilder.AppendLine ($"{numerator}/{denominator}");
                }
            }
            else
            {
                resultingStringBuilder.AppendLine ($"{numerator}");
            }
        }

        public void WriteFractionDebug()
        {
            if (denominator != 1)
            {
                if (denominator < 0)
                {
                    Console.WriteLine($"Fraction is: {-numerator}/{-denominator}. Numerator: {-numerator}, Denominator: {-denominator}");
                }
                else
                {
                    Console.WriteLine($"Fraction is: {numerator}/{denominator}. Numerator: {numerator}, Denominator: {denominator}");
                }
            }
            else
            {
                Console.WriteLine($"Fraction is: {numerator}. Numerator: {numerator}, Denominator: {denominator}");
            }
        }


        public void ClearState()
        {
            this.numerator = 0;
            this.denominator = 0;
            isWholeZero = false;
            ZeroDivisionOccured = false;
        }

        public bool ZeroDivision()
        {
            if (this.denominator == 0)
                return true;
            else
                return false;
        }


        public static int LeastCommonMultiple(int a, int b)
        {
            if (a == 0 || b == 0)
            return 0;
            for (int i = 1; i <= a && i <= b; ++i)
            {
                if (a % i == 0 && b % i == 0)
                {
                    return (a * b) / i;
                }
            }
            // If no suitable number is found, return 1
            return 1;
        }

        public static int GreatestCommonDivisor(int a, int b)
        {
            while (b != 0)
            {
                int temp = b;
                b = a % b;
                a = temp;
            }

            return a;
        }

        // public bool IfExists()
        // {
        //     return denominator != 0 || numerator != 0 ? true : false;
        // }

        public bool IfExists()
        {
            return denominator + numerator != 0 ? true : false;
        }

        public int GetNumerator
        {
            get { return numerator; }
        }

        public int GetDenominator
        {
            get { return denominator; }
        }

    }

    public class Arithmetics
    {
        public Fraction resultingFraction = new();

        // private int numeratorA = 0; 
        private int denominatorA = 0;

        // private int numeratorB = 0; 
        private int denominatorB = 0;

        public string result = "";

        public Fraction MultiplyFractions(Fraction A, Fraction B)
        {
            if (B.GetDenominator == 0 || A.GetDenominator == 0)
            {
                resultingFraction.ZeroDivisionOccured = true;
                return resultingFraction;
            }
            else if ((A.GetNumerator == 0 || B.GetNumerator == 0))
            {
                resultingFraction.isWholeZero = true;
                resultingFraction.SetFraction(0, 1);
                return resultingFraction;
            }
            resultingFraction.SetFraction(A.GetNumerator * B.GetNumerator, A.GetDenominator * B.GetDenominator);

            resultingFraction.Simplify();

            return resultingFraction;
        }

        public Fraction DivideFractions(Fraction A, Fraction B)
        {
            if ((A.GetNumerator == 0 && B.GetNumerator == 0))
            {
                resultingFraction.ZeroDivisionOccured = true;
                return resultingFraction;
            }
            if (B.GetNumerator == 0)
            {
                resultingFraction.ZeroDivisionOccured = true;
                return resultingFraction;
            }
            if (B.GetDenominator == 0 || A.GetDenominator == 0)
            {
                resultingFraction.ZeroDivisionOccured = true;
                return resultingFraction;
            }
            if (A.GetNumerator == 0 && B.GetNumerator != 0)
            {
                resultingFraction.isWholeZero = true;
                resultingFraction.SetFraction(0, 1);
                return resultingFraction;
            }
            if (B.GetNumerator == 0 && A.GetNumerator != 0)
            {
                resultingFraction.ZeroDivisionOccured = true;
                return resultingFraction;
            }

            resultingFraction.SetFraction(A.GetNumerator * B.GetDenominator, A.GetDenominator * B.GetNumerator);

            // if (resultingFraction.GetDenominator == 0 && resultingFraction.GetNumerator == 0)
            // {
            //     resultingFraction.isWholeZero = true;
            //     resultingFraction.SetFraction(0, 1);

            // }

            resultingFraction.Simplify();

            return resultingFraction;
        }

        public Fraction AddFractions(Fraction A, Fraction B)
        {
            if (A.GetNumerator == 0 && A.GetDenominator == 1 && B.GetNumerator == B.GetDenominator)
            {
                // B.Simplify();
                resultingFraction.isWholeZero = true;
                resultingFraction.SetFraction(1, 1);
                return resultingFraction;
            }
            if (A.GetDenominator == 0 || B.GetDenominator == 0 )
            {
                resultingFraction.ZeroDivisionOccured = true;
                return resultingFraction;
            }
            if (B.GetNumerator == 0 && A.GetNumerator == 0)
            {
                B.isWholeZero = true;
                A.isWholeZero = true;
                resultingFraction.SetFraction(0, 1);
                resultingFraction.isWholeZero = true;
                return resultingFraction;
            }
            if (A.GetNumerator == 0 && B.GetNumerator != 0)
            {
                A.isWholeZero = true;
                resultingFraction.SetFraction(B.GetNumerator, B.GetDenominator);
                return resultingFraction;
            }
            if (B.GetNumerator == 0 && A.GetNumerator != 0)
            {
                B.isWholeZero = true;
                resultingFraction.SetFraction(A.GetNumerator, A.GetDenominator);
                return resultingFraction;
            }
            if (A.GetDenominator == B.GetDenominator)
            {
                A.Simplify();
                B.Simplify();
            resultingFraction.SetFraction(A.GetNumerator + B.GetNumerator, A.GetDenominator);
            }
            else {
            // int gcd = Fraction.GreatestCommonDivisor(A.GetDenominator, B.GetDenominator);
            resultingFraction.SetFraction(A.GetNumerator * B.GetDenominator + B.GetNumerator * A.GetDenominator, A.GetDenominator * B.GetDenominator);
            }

            resultingFraction.Simplify();

            return resultingFraction;
        }
        
        public Fraction SubtractFractions(Fraction A, Fraction B)
        {
            // if (A.GetDenominator != 0 || B.GetDenominator != 0)
            // {
            //    A.Simplify();
            //    B.Simplify();
            // }
            if (A.GetNumerator == 0 && A.GetDenominator == 1 && B.GetNumerator == B.GetDenominator)
            {
                // B.Simplify();
                // resultingFraction.ClearState();
                resultingFraction.SetFraction(-1, 1);
                return resultingFraction;
            }
            if (A.GetNumerator == 0 && B.GetNumerator == B.GetDenominator)
            {
                // B.Simplify();
                resultingFraction.SetFraction(-1, 1);
                return resultingFraction;
            }
            if (A.GetDenominator == 0 || B.GetDenominator == 0)
            {
                resultingFraction.ZeroDivisionOccured = true;
                return resultingFraction;
            }
            if (B.GetNumerator == 0 && A.GetNumerator == 0)
            {
                B.isWholeZero = true;
                A.isWholeZero = true;
                resultingFraction.SetFraction(0, 1);
                resultingFraction.isWholeZero = true;
                return resultingFraction;
            }
            if (A.GetNumerator == 0 && B.GetNumerator != 0)
            {
                A.isWholeZero = true;
                resultingFraction.SetFraction(-B.GetNumerator, B.GetDenominator);
                resultingFraction.Simplify();
                return resultingFraction;
            }
            if (A.GetNumerator != 0 && B.GetNumerator == 0)
            {
                B.isWholeZero = true;
                resultingFraction.SetFraction(A.GetNumerator, A.GetDenominator);
                resultingFraction.Simplify();
                return resultingFraction;
            }

           if (A.GetDenominator == B.GetDenominator)
           {
            resultingFraction.SetFraction(A.GetNumerator - B.GetNumerator, A.GetDenominator);
            // resultingFraction.SetFraction(777, 775);
           }
           else {
            // int gcd = Fraction.GreatestCommonDivisor(A.GetDenominator, B.GetDenominator);
            if (A.GetNumerator == 0)
            {
                resultingFraction.SetFraction((B.GetNumerator), B.GetDenominator);
            } else {

            resultingFraction.SetFraction(A.GetNumerator * B.GetDenominator - B.GetNumerator * A.GetDenominator, A.GetDenominator * B.GetDenominator);
            }
            
            // resultingFraction.SetFraction(777,777);
           }

            resultingFraction.Simplify();
            // resultingFraction.SetFraction(777,777);

            return resultingFraction;
        }

        public string CompareFractions(Fraction A, Fraction B, string ComparisonOperator){

            if (B.GetDenominator == 0 || A.GetDenominator == 0)
            {
                result = "nelze";
                return result;
            }

            int lcm = denominatorA = denominatorB = Fraction.LeastCommonMultiple(A.GetDenominator, B.GetDenominator);

            A.SetFraction(lcm / A.GetDenominator * A.GetNumerator, denominatorA);
            B.SetFraction(lcm / B.GetDenominator * B.GetNumerator, denominatorB);
            
            if (A.GetDenominator == B.GetDenominator)
            {
                if (ComparisonOperator == ">")
                {
                    // Perform logic if the comparison operator is ">"

                    result = A.GetNumerator > B.GetNumerator ? "true": "false";
                    return result;

                } else if (ComparisonOperator == "<")
                {
                    result = A.GetNumerator < B.GetNumerator ? "true": "false";
                    return result;

                } else
                {
                    result = A.GetNumerator == B.GetNumerator ? "true": "false";
                    return result;
                    
                } 
            } else
            {
                return "1";
            }
            
        }

        public Fraction RoundAndDivide(Fraction A)
        {
            if (A.GetDenominator == 0)
            {
                resultingFraction.ZeroDivisionOccured = true;
                return resultingFraction;
            }

            // if (A.GetNumerator == 0)
            // {
            //     resultingFraction.SetFraction(0, 1);
            //     resultingFraction.isWholeZero = true;
            //     return resultingFraction;
            // }

            int numerator = (int) Math.Floor((double) A.GetNumerator / A.GetDenominator);
            int denominator = 1;
            
            resultingFraction.SetFraction(numerator, denominator);
            // resultingFraction.SetFraction(777, 777);

            return resultingFraction;
        }


    }

    class Service
    {
        // хз зачем, но int тут было удалено
        string[] operationSet = {"+","-","*",">","<","\\","=", "int"};
        
        // string[] operationSet = {"+","-","*",">","<","\\","="};
        public string operationSign = "";
        public string line = "";
        // string result = "";
        public bool DevidedZero = false;
        public bool SpecialCase = false;

        public string finalResult = "";
        
        Fraction A = new();
        Fraction B = new();
        public Arithmetics arithmetics = new();

        public string currentOperandLine
        {
            get { return line; }
            set { line = value; }
        }

        public string currentOperand
        {
            get { return operationSign; }
            set { operationSign = value; }
        }

        public void DoAll(StringBuilder resultingStringBuilder)
        {
            ExtractOperand();
            ExtractFractions();
            if (A.ZeroDivision() || B.ZeroDivision() || B.GetNumerator == 0)
            {
                DevidedZero = true;
            }
            if (!B.IfExists()) // На что-то влияет?
            {
                DevidedZero = false;
            }
            if (A.isWholeZero || B.isWholeZero)
            {
                DevidedZero = false;
            }

            switch (operationSign)
            {
                case "+":
                    arithmetics.AddFractions(A, B);
                    break;
                case "-":
                    arithmetics.SubtractFractions(A, B);
                    // arithmetics.resultingFraction.SetFraction(777,777);
                    break;
                case "*":
                    arithmetics.MultiplyFractions(A, B);
                    break;
                case "\\":
                    // arithmetics.resultingFraction.ZeroDivisionOccured = false;
                    arithmetics.DivideFractions(A, B);
                    break;
                 case ">":
                    arithmetics.result = "";
                    arithmetics.CompareFractions(A, B, ">");
                    break;
                case "<":
                    arithmetics.result = "";
                    arithmetics.CompareFractions(A, B, "<");
                    break;
                case "=":
                    arithmetics.result = "";
                    arithmetics.CompareFractions(A, B, "=");
                    break;
                case "int":
                    arithmetics.result = "";
                    arithmetics.RoundAndDivide(A);
                    break;
            }

            if (Math.Abs(arithmetics.resultingFraction.GetDenominator) == 1 && Math.Abs(arithmetics.resultingFraction.GetNumerator) == 1)
            {
                SpecialCase = true;
            }

            if (arithmetics.resultingFraction.isWholeZero)
            {
                arithmetics.resultingFraction.WriteFractionToLine(resultingStringBuilder);
            }
            else if(arithmetics.resultingFraction.IfExists() && !arithmetics.resultingFraction.ZeroDivisionOccured)
            {
                arithmetics.resultingFraction.WriteFractionToLine(resultingStringBuilder);
            }
            else if(DevidedZero == true || arithmetics.resultingFraction.ZeroDivisionOccured)
            {
                resultingStringBuilder.AppendLine("nelze");
            } 
            else if (arithmetics.result != "")
            {
                resultingStringBuilder.AppendLine(arithmetics.result);
            } else if ( SpecialCase && !arithmetics.resultingFraction.ZeroDivisionOccured)
            {
                arithmetics.resultingFraction.WriteFractionToLine(resultingStringBuilder);
            }
            // if (arithmetics.resultingFraction.GetDenominator == 1 && arithmetics.resultingFraction.GetNumerator == -1)
            // {
            //     arithmetics.resultingFraction.SetFraction(-1,1);
            //     arithmetics.resultingFraction.WriteFractionToLine(resultingStringBuilder);
            // }
            // if (arithmetics.resultingFraction.GetDenominator == -1 && arithmetics.resultingFraction.GetNumerator == 1)
            // {
            //     arithmetics.resultingFraction.SetFraction(-1,1);
            //     arithmetics.resultingFraction.WriteFractionToLine(resultingStringBuilder);
            // }

            arithmetics.resultingFraction.ClearState();
            arithmetics.resultingFraction.ZeroDivisionOccured = false;
            DevidedZero = false;
            A.ClearState();
            B.ClearState();
        }

        public void ExtractOperand()
        {
            foreach (string operand in operationSet)
            {
                if (line.Contains(operand))
                currentOperand = operand;
            }
        }

        public void ExtractFractions()
        {
            string[] fractions = {};
            int numeratorA, denominatorA, numeratorB, denominatorB;
            bool RoundFlag = false;


            if (line.Contains("int"))
            {
                RoundFlag = true;
            } else
            {
                fractions = line.Split(operationSign);
            }

            if (fractions.Length == 2)
            {

            string[] partsA = fractions[0].Split('/');
            string[] partsB = fractions[1].Split('/');

                bool lengthEquals1 = true;

                if (partsA.Length == 1 && partsB.Length == 2)
                { 
                    if (int.TryParse(partsA[0], out numeratorA) && int.TryParse(partsB[0], out numeratorB) && int.TryParse(partsB[1], out denominatorB))
                    {
                        if (numeratorA == 0)
                        {
                            A.isWholeZero = true;
                        }
                        A.SetFraction(numeratorA, 1);
                        B.SetFraction(numeratorB, denominatorB);
                        
                    }

                    lengthEquals1 = false;
                
                } 
                if(partsB.Length == 1 && partsA.Length == 2){

                    if (int.TryParse(partsA[0], out numeratorA) && int.TryParse(partsA[1], out denominatorA) && int.TryParse(partsB[0], out numeratorB))
                    {
                        if (numeratorB == 0)
                        {
                            B.isWholeZero = true;
                        }
                        A.SetFraction(numeratorA, denominatorA);
                        B.SetFraction(numeratorB, 1);
                    }
                    lengthEquals1 = false;
                }
                if(partsA.Length == 1 && partsB.Length == 1){

                    if (int.TryParse(partsA[0], out numeratorA) && int.TryParse(partsB[0], out numeratorB))
                    {
                        if (numeratorB == 0)
                        {
                            B.isWholeZero = true;
                        }
                        if (numeratorA == 0)
                        {
                            A.isWholeZero = true;
                        }
                        A.SetFraction(numeratorA, 1);
                        B.SetFraction(numeratorB, 1);
                    }
                    lengthEquals1 = false;
                }
                if(partsA.Length == 2 && partsB.Length == 0){

                    if (int.TryParse(partsA[0], out numeratorA) && int.TryParse(partsA[1], out denominatorA))
                    {
                        if (numeratorA == 0)
                        {
                            A.isWholeZero = true;
                        }
                        A.SetFraction(numeratorA, denominatorA);
                    }
                    lengthEquals1 = false;
                }

                if (lengthEquals1 && int.TryParse(partsA[0], out numeratorA) && int.TryParse(partsA[1], out denominatorA) && int.TryParse(partsB[0], out numeratorB) && int.TryParse(partsB[1], out denominatorB))
                {
                    if (numeratorB == 0)
                        {
                            B.isWholeZero = true;
                        }
                    if (numeratorA == 0)
                    {
                        A.isWholeZero = true;
                    }

                    A.SetFraction(numeratorA, denominatorA);
                    B.SetFraction(numeratorB, denominatorB);
                    // Console.WriteLine(partsA.Length +" "+partsB.Length);
                }
            } 
            
            if(RoundFlag)
            {
                // A.SetFraction(777, 777);
                // B.SetFraction(0, 0);
                // string insideInt = fractions[0].Substring(fractions[0].IndexOf("(") + 1, fractions[0].Length - fractions[0].IndexOf("(") - 2);

                // string[] littleFraction = insideInt.Split('/');

                string pattern = @"int\((\d+)/(\d+)\)";
                Match match = Regex.Match(line, pattern);
                if (match.Success)
                {
                    string numerator = match.Groups[1].Value;
                    string denominator = match.Groups[2].Value;
                    A.SetFraction(Convert.ToInt32(numerator), Convert.ToInt32(denominator));
                    B.SetFraction(0, 0);
                }

                // A.SetFraction(Convert.ToInt32(littleFraction[0]), Convert.ToInt32(littleFraction[1]));
                // B.SetFraction(0, 0);
            }
        }
    }
    class Program
    {
        static void Main(string[] args)
        {
            // Reading content of the file
            StreamReader Reader = new StreamReader("vstup.txt");
            string content = Reader.ReadToEnd();
            Reader.Close();

            // Splitting it line by line
            string[] lines = content.Split('\n');

            // Creating an object
            Service service = new Service();

             // String for saving the result
            StringBuilder resultingStringBuilder = new StringBuilder();

            // Create a new StreamWriter object to write the output to the file
            // StreamWriter Writer = new StreamWriter("vystup.txt");

            // line by line transfer to processing class
            foreach (string line in lines)
            {
                service.currentOperandLine = line;
                service.DoAll(resultingStringBuilder);

                // Write the output to the file
                // Writer.WriteLine(service.outputString);
            }

            StreamWriter Writer = new StreamWriter("vystup.txt");
            Writer.Write(resultingStringBuilder.ToString());
            Writer.Close();

            // Console.WriteLine("Done writing to file.");
        }
    }
}