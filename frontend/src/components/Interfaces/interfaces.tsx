
export interface Publisher {
    id: number,
    name: string,
}

export interface DeveloperTeam {
    id: number,
    name: string,
}

export interface Genre {
    id: number,
    name: string,
}

export interface Game {
    id: number,
    title: string,
    genres: Genre[],
    cover_url: string,
    publisher?: string,
    developer?: string,    
}

