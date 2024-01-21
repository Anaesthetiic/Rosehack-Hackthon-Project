#include <string>

class Player 
{
    private:
        string currCity;

    public:
        Player();                       // Default Constructor
        Player(string currCity);        // Argument Constructor

        string getCurrCity() const;     // Accessor
};