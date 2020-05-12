using Google.Protobuf;
using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Tutorial;

namespace ConsoleApp1
{
    class Program
    {

        private static byte[] GetByteArray(Person person)
        {
            using (var ms = new MemoryStream())
            {
                person.WriteTo(ms);
                return ms.ToArray();
            }
        }

        private static Person GetPersonFromByteArray(byte[] bytes)
        {
            return Person.Parser.ParseFrom(bytes);
        }

        static void Main(string[] args)
        {
            // The code provided will print ‘Hello World’ to the console.
            // Press Ctrl+F5 (or go to Debug > Start Without Debugging) to run your app.
            Console.WriteLine("Hello World!");
            

            // Go to http://aka.ms/dotnet-get-started-console to continue learning how to build a console app! 

            Person john = new Person
            {
                Id = 1234,
                Name = "John Doe",
                Email = "jdoe@example.com",
                Phones = { new Person.Types.PhoneNumber { Number = "555-4321", Type = Person.Types.PhoneType.Home } }
            };

            byte[] bytes = GetByteArray(john);
            Person deserailized = GetPersonFromByteArray(bytes);
            Console.WriteLine(deserailized.Name);

            Console.ReadKey();
        }
    }
}
