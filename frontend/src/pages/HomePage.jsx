import { useState, useEffect } from 'react';
import { Link } from 'react-router-dom'; // Importamos Link

function HomePage() {
  const [professionals, setProfessionals] = useState([]);

  useEffect(() => {
    const fetchProfessionals = async () => {
      try {
        const response = await fetch('https://guia-backend-806646797715.southamerica-east1.run.app/api/professionals/');
        const data = await response.json();
        setProfessionals(data);
      } catch (error) {
        console.error("Error al obtener los profesionales:", error);
      }
    };
    fetchProfessionals();
  }, []);

  return (
    <>
      <h1>Guía de Profesionales</h1>
      <div className="card-container">
        {professionals.map(prof => (
          // Cada profesional ahora es un link a su página de detalle
          <Link to={`/professional/${prof.id}`} key={prof.id} className="card-link">
            <div className="card">
              <h2>{prof.full_name}</h2>
              <p><strong>Especialidad:</strong> {prof.specialty}</p>
            </div>
          </Link>
        ))}
      </div>
    </>
  );
}
export default HomePage;