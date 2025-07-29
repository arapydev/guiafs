import { useState, useEffect } from 'react';
import { useParams, Link } from 'react-router-dom'; // useParams para leer la URL

function DetailPage() {
  const [professional, setProfessional] = useState(null);
  const { id } = useParams(); // Obtenemos el ID del profesional de la URL

  useEffect(() => {
    const fetchProfessional = async () => {
      try {
        const response = await fetch(`https://guia-backend-806646797715.southamerica-east1.run.app/api/professionals/${id}/`);
        const data = await response.json();
        setProfessional(data);
      } catch (error) {
        console.error("Error al obtener el detalle:", error);
      }
    };
    fetchProfessional();
  }, [id]); // El efecto se ejecuta de nuevo si el ID cambia

  if (!professional) {
    return <p>Cargando...</p>;
  }

  return (
    <>
      <Link to="/">&larr; Volver a la lista</Link>
      <div className="card detail-card">
        <h1>{professional.full_name}</h1>
        <p><strong>Especialidad:</strong> {professional.specialty}</p>
        <p><strong>Biografía:</strong> {professional.bio}</p>
        <p><strong>Email:</strong> {professional.email}</p>
        <p><strong>Teléfono:</strong> {professional.phone_number}</p>
        <p><strong>Dirección:</strong> {professional.address}</p>
        <div>
          <strong>Categorías:</strong>
          <ul>
            {professional.categories.map(cat => (
              <li key={cat.id}>{cat.name}</li>
            ))}
          </ul>
        </div>
      </div>
    </>
  );
}
export default DetailPage;