#pragma once
#include "Tile.h"

class DirtTile : public Tile {
    friend class Tile;

public: //was previously protected, for CML testing
    DirtTile(int id);
};