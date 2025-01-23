import React from 'react';
import styles from './table.module.css';

const TablePage = ({ data }) => {
  return (
    <div>
      <h1>Files Table</h1>
      <table className={styles.table}>
        <thead>
          <tr>
            <th className={styles.header}>File ID</th>
            <th className={styles.header}>File Name</th>
            <th className={styles.header}>File Path</th>
            <th className={styles.header}>Updated At</th>

          </tr>
        </thead>
        <tbody>
          {data.map((file) => (
            <tr key={file.id} className={styles.row}>
              <td className={styles.cell}>{file.id}</td>
              <td className={styles.cell}>{file.file_name}</td>
              <td className={styles.cell}>{file.file_path}</td>
              <td className={styles.cell}>{file.created_at}</td>

            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default TablePage;
