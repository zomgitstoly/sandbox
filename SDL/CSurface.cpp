#include "CSurface.h"

CSurface::CSurface(){

}

SDL_Surface* CSurface::OnLoad(char* File){
	SDL_Surface* Surf_Temp = NULL;
	SDL_Surface* Surf_Return = NULL;

	if((Surf_Temp = SDL_LoadBMP(File)) == NULL){
		return NULL;
	}

	Surf_Return = SDL_DispalyFormat(Surf_Temp);
	SDL_FreeSurface(Surf_Temp);
	
	return Surf_Return;
}

