/*
Codewars Coding Challenge

Return location

You are given a class named Person with a method named location, which should return the 3D location of the given person.

Can you find the bug?

class Person
{
    public:
        Person(int x, int y, int z)
            : m_x(x), m_y(y), m_z(z)
        {
        }
        
        void location(int x, int y, int z)
        {
            x = m_x;
            y = m_y;
            z = m_z;
        }
        
    private:
        int m_x;
        int m_y;
        int m_z;
};

https://www.codewars.com/kata/57f037927b45ef77b3000260/train/cpp
*/

// My Solution
class Person
{
    public:
        Person(int x, int y, int z)
            : m_x(x), m_y(y), m_z(z)
        {
        }
        
        void location(int& x, int& y, int& z)
        {
            x = m_x;
            y = m_y;
            z = m_z;
        }
        
    private:
        int m_x;
        int m_y;
        int m_z;
};


/*
Sample Test

Describe(person_test)
{
    It(should_return_location)
    {
        Person* person = new Person(1, 2, 3);
        int x = 0, y = 0, z = 0;
        person->location(x, y, z);
        Assert::That(x, Equals(1));
        Assert::That(y, Equals(2));
        Assert::That(z, Equals(3));
    }
};

*/