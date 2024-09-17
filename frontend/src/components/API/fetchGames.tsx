import { useEffect, useState } from "react";
import { Game } from "../Interfaces/interfaces";

const API_URL = '/api/v1';

const GamesList = () => {
    const [games, setGames] = useState<Game[]>([]);
    const [error, setError] = useState<string | null>(null);
    
    useEffect(() => {
        const fetchGames = async() => {
            try {
                const response = await fetch(`${API_URL}/games/`);
                if (!response.ok) {
                    const text = await response.text();
                    throw new Error(`Error: ${text}`);
                }

                const contentType = response.headers.get("content-type");
                if (!contentType || !contentType.includes("application/json")) {
                        throw new Error("Response is not Json")
                }
                const data = await response.json();
                setGames(data);
            }   catch(err: any) {
                    setError(err.message);
                }
        };

        fetchGames();
    }, []);
    
    
    return (
        <div>
            <h1>Game List</h1>
            {error ? <p>Error: {error}</p>: null}
            <ul>
                {games.map((game) => ( 
                    <li key={game.id}>{game.title}</li>
                ))}
            </ul>
        </div>
    )
}

export default GamesList