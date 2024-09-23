import React from "react";
import "./GameCard.css";
// import { DeveloperTeam } from "../Interfaces/interfaces";

interface GameCardProps {
    id: number,
    title: string,
    genres: string[],
    developer: string,
    cover_url: string,
}

const GameCard: React.FC<GameCardProps> = ({title, cover_url, genres, developer}) => {
  return (
    <div className="game-card">
        <img className="game-image" src={cover_url} alt={title} />
        <div className="game-card-details">
            <h3 className="game-card-title">{title}</h3>
            <p className="game-card-genres">
              {genres.join(", ")}
            </p>
            <p className="game-card-developer">Developer: {developer}</p>
        </div>
    </div>
  )
}

export default GameCard