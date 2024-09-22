import React from "react";
import { Link } from "react-router-dom";
import "./GameCard.css";

interface GameCardProps {
    id: number,
    title: string,
    genres: string[],
    cover_url: string,
}

const GameCard: React.FC<GameCardProps> = ({id, title, cover_url}) => {
  return (
    <div className="game-card">
        <img className="game-image" src={cover_url} alt={title} />
        <div className="game-card-details">
            <Link to={`games/${id}`}>{title}</Link>
        </div>
    </div>
  )
}

export default GameCard