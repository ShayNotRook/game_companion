import { useEffect, useState } from 'react';
import { fetchGames } from '../../API/fetchGames';
import GameCard from '../GameCard';
import './GamesList.css';
import { DeveloperTeam } from '../../Interfaces/interfaces';

interface Game {
    id: number,
    title: string,
    developer: string,
    genres: string[],
    cover_url: string,
}

const GameList: React.FC = () => {
    const [games, setGames] = useState<Game[]>([]);
    const [loading, setLoading] = useState<boolean>(true);

    useEffect(() => {
        const loadGames = async () => {
            try {
                const data = await fetchGames();
                setGames(data);
            } catch (error) {
                console.log('Error loading games:', error);
            } finally {
                setLoading(false);
            }
        };

        loadGames();
    }, []);


    if (loading) {
        return <div>Loading...</div>
    }

    return (
            <div className='game-list'>
                {games.length > 0 ? (
                    games.map((game) => (
                        <GameCard
                            key={game.id}
                            id={game.id}
                            title={game.title}
                            genres={game.genres}
                            developer={game.developer}
                            cover_url={game.cover_url}
                        />
                    ))
                ) : (
                    <p className='no-games'>No games available.</p>
                )}
            </div>
    );
};

export default GameList