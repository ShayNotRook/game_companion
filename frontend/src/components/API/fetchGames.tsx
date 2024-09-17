
const API_URL = 'http://localhost:8000/api/v1';

export const fetchGames = async() => {
try {
    const response = await fetch(`${API_URL}/games/`);
    if (!response.ok) {
            const text = await response.text();
            throw new Error(`Error: ${text}`);
        }

    const contentType = response.headers.get("content-type");
    if (!contentType || !contentType.includes("application/json")) {
            throw new Error("Response")
    }
    const data = await response.json();
    return data;
    } catch(error) {
        console.log(error)
    }
};
    // return (
    //     <div>
    //         <h1>Game List</h1>
    //         {/* {error ? <p>Error: {error}</p>: null} */}
    //         <ul>
    //             {games.map((game) => ( 
    //                 <li key={game.id}>
    //                     <img src={game.cover_url} />
    //                     {game.title}
    //                 </li>
    //             ))}
    //         </ul>
    //     </div>
    // )
