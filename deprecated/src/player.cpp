#include "header/player.hpp"

using namespace std;

Player::Player()
{
    currCity = "null";
}

Player::Player(string currCity)
{
    this->currCity = currCity;
}

string Player::getCurrCity() const
{
    return currCity;
}