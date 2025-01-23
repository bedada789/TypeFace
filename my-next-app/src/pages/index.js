import { useEffect, useState } from 'react';
import styles from './table.module.css';
import TablePage from './list';

export default function Home() {
  const [customName, setCustomName] = useState('');
  const [selectedFile, setSelectedFile] = useState(null);

  const [files, setFiles] = useState([]);

  // Function to fetch files
  const fetchFiles = async () => {
    try {
      const response = await fetch('http://127.0.0.1:8000/api/list_files');
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }
      const data = await response.json();
      
      
      setFiles(data['list']); 
    } catch (error) {
      console.error('Error fetching files:', error);
    }
  };
  const handleFileChange = (e) => {
    setSelectedFile(e.target.files[0]);
  };

  const handleNameChange = (e) => {
    setCustomName(e.target.value);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!selectedFile || !customName) {
      alert('Please provide a file and a custom name.');
      return;
    }

    const formData = new FormData();
    formData.append('file', selectedFile);
    formData.append('custom_name', customName);

    try {
      const uploadResponse = await fetch('http://127.0.0.1:8000/api/upload_file', {
        method: 'POST',
        body: formData,
      });

      if (uploadResponse.ok) {
        const uploadData = await uploadResponse.json();
        const fileUrl = uploadData.file_url;

        const createResponse = await fetch('http://127.0.0.1:8000/api/create_file', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({
            file_path: fileUrl,
            file_name: customName,
          }),
        });

        if (createResponse.ok) {
          console.log('File record created successfully');
          // Fetch the updated list of files
          fetchFiles();
        } else {
          console.error('Error creating file record:', createResponse.statusText);
        }
      } else {
        console.error('Error uploading file:', uploadResponse.statusText);
      }
    } catch (error) {
      console.error('Error:', error);
    }
  };


  useEffect(() => {
    fetchFiles();
  }, []);

  return (
    <div className={styles.headers}>
      <form onSubmit={handleSubmit} className={styles.upload_file}>
        <label htmlFor="customName" className={styles.text}>
          Custom File Name:
        </label>
        <input
          type="text"
          id="customName"
          value={customName}
          onChange={handleNameChange}
          required
        />
        <label htmlFor="fileUpload" className={styles.text}>
          Choose File:
        </label>
        <input
          type="file"
          id="fileUpload"
          onChange={handleFileChange}
          required
        />
        <button type="submit" className={styles.button}>
          Upload
        </button>
      </form>
      <TablePage data={files} />
    </div>
  );
}
