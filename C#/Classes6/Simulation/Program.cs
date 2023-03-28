using System;

namespace Exams
{
    internal class Programm
    {
        class Teacher
        {
            public int MinutesPerPage;

            public Teacher(int MinutesPerPage)
            {

                this.MinutesPerPage = MinutesPerPage;
            }
        }

        class Test
        {
            int Pages;

            public Test(int Pages)
            {

                this.Pages = Pages;
            }
        }

        class Event
        {
            Teacher teacher;
            Test test;

            int endTime;

            public Event(Teacher teacher, Test test, int endTime)
            {

                this.teacher = teacher;
                this.test = test;
                this.endTime = endTime;
            }

            public void Process(){

                Console.WriteLine(ev.ToString());
            }

            public override string ToString()
            {
                return "Teacher fixed test at " + endTime + "minutes";
            }
        }

        class Calendar
        {

            public AddEvent(Event ev)
            {

            }

            public Event ExtractMin()
            {

            }

            public bool IsEmpty()
            {

            }

        }

        static void Main(string[] args)
        {
            Stack<Test> tests = new Stack<Test>();
            for (int i = 0; i < 10; i++)
            {
                tests.Push(new Test(5));
            }

            Teacher[] teachers = {new Teacher(1), new Teacher(3), new Teacher(15)};

            // ----------------

            Calendar calendar = new Calendar();

            foreach (Teacher te in teachers)
            {
                Test test = tests.Pop();
                calendar.AddEvent(new Event(
                    teacher, 
                    test, 
                    teacher.MinutesPerPage * test.Pages()));
            }

            while (true)
            {
                Event ev = calendar.ExtractMin();

                ev.Process();

                Test test = tests.Pop();
                calendar.AddEvent(new Event(ev.teacher, test, ev.EndTime + ev.teacher.MinutesPerPage * test.Pages));
            }
        }
    }
}