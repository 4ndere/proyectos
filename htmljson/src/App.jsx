import './App.css'
import './bootstrap.min.css'

import Records from './ProfileClient.json'

function App() {
  return (
    <div className="App">
      {
        Records && Records.map(record => {
          return (
            <div className='box' key={record.id}>
              <div className="flex">
                <th>ID:
                  <br></br>{record.id}
                </th>
              </div>
              <div>
                <th>Punto:
                  <br></br>{record.title}
                </th>
              </div>
            </div>
          )
        })
      }

    </div>
  )
}

export default App
