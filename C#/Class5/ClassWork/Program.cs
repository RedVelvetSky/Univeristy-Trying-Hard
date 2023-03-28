using System;

namespace ComplexNumbers
{
    interface IComplex
    {
        IComplex Add(IComplex c);

        IComplex Sub(IComplex c);

        IComplex Mul(IComplex c);

        IComplex Square(IComplex c);

        double Norm();

        double Real {get;}
        double Imaginary {get;}
    }

    class Complex : IComplex
    {

        private double real;
        private double imaginary;

        public double Real {get => real;}
        
        public double Imaginary {get => imaginary;}
        
        public Complex(double real, double imaginary){
            this.real = real;
            this.imaginary = imaginary;
        }

        public IComplex Add(IComplex c)
        {
            double realSum = this.Real + c.Real;
            double imaginarySum = this.Imaginary + c.Imaginary;

            return new Complex(realSum, imaginarySum);
        }

        public IComplex Sub(IComplex c)
        {
            double realSub = this.Real - c.Real;
            double imaginarySub = this.Imaginary - c.Imaginary;

            return new Complex(realSub, imaginarySub);
        }

        public IComplex Mul(IComplex c)
        {
            double realProduct = (this.real *c.Real) - (this.imaginary *c.Imaginary);
            double imagProduct = (this.real *c.Imaginary) + (this.imaginary *c.Real);

            return new Complex(realProduct, imagProduct);
        }

        public IComplex Square(IComplex c)
        {
            double realSquared = (this.real * this.real) - (this.imaginary * this.imaginary);
            double imagSquared = 2 * (this.real * this.imaginary);

            return new Complex(realSquared, imagSquared);
        }

        public double Norm()
        {
            double norm = (this.real * this.real) + (this.imaginary * this.imaginary);
             
            return Math.Sqrt(norm);
        }

        public override string ToString()
        {
            return $"{Real} + {Imaginary}i";
        }
    }

    internal class Program
    {
        static void Main(string[] args)
        {
            Complex complex1 = new Complex(2, 2);
            Complex complex2 = new Complex(3, 5);

            IComplex sum = complex1.Add(complex2);
            Console.WriteLine(sum);

            IComplex sub = complex1.Sub(complex2);
            Console.WriteLine(sub);

            IComplex mul = complex1.Mul(complex2);
            Console.WriteLine(mul);

            IComplex square = complex1.Square(complex2);
            Console.WriteLine(square);
            
            double norm = complex1.Norm();
            Console.WriteLine(norm);
        }
    }
}