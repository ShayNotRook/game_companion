import './App.css'
import { BrowserRouter as Router, Routes, Route} from 'react-router-dom';

import GamesList from './components/Games/List/GameList';
import Home from './components/Main/Home';
import Header from './components/Main/Partials/Header';

function App() {

  return (
    <Router>
      <div className='App'>
        <Header />
        <Routes>
          <Route path='' element={<Home />}/>
          <Route path='/games' element={<GamesList />}/>
        </Routes>
      </div>    
    </Router>
  )
};

export default App
