import { useEffect, useState } from 'react';
import { fetchGames } from '../../API/fetchGames';
import GameCard from '../GameCard';

interface Game {
    id: number,
    title: string,
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
            {games.map((game) => (
                <GameCard
                    key={game.id}
                    id={game.id}
                    title={game.title}
                    genres={game.genres}
                    cover_url={game.cover_url}
                />
            ))}
        </div>
    );
};

export default GameList