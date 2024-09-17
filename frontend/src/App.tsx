import './App.css'
import { BrowserRouter as Router, Routes, Route} from 'react-router-dom';

import GamesList from './components/Games/List/GameList';

function App() {

  return (
    <Router>
      <div className='App'>
        <Routes>
          <Route path='/games' element={<GamesList />}/>
        </Routes>
      </div>    
    </Router>
  )
};

export default App
