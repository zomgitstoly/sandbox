#ifndef _CSURFACE_H_
#define _CSURFACE_H_
#include <SDL.h>

class CSurface {
	public:
		CSurface();
	public:
		static SDL_Surface* OnLoad(char* File);
};
#endif
