#include <iostream>
#include "player.hpp"

using namespace std;

int main()
{
    testPlayerClass();
}

void testPlayerClass()
{
    Player testPlayer("Riverside County");

    cout << testPlayer.getCurrCity() << endl;
}