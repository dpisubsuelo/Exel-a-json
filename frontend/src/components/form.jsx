import { useState } from "react";

const Upfile = () => {
    const [file, setFile] = useState(null);

    const handleFileInputChange = (event) => {
        setFile(event.target.files[0]);
    };

    const handleSubmit = async (event) => {
        event.preventDefault();

        const formData = new FormData();
        formData.append("file_upload", file);

        try {
            const endpoint = "http://localhost:8000/uploadfile/";
            const response = await fetch(endpoint, {
                method: "POST",
                body: formData,
            });

            if (response.ok) {
                console.log("File uploaded successfully", response);
                alert("File uploaded successfully");
            } else {
                console.error("Failed to upload file");
            }
        } catch (error) {
            console.error(error);
        }
    };

    return (
        <div>
            <h1> Enviar archivo </h1>
            <form className="form" onSubmit={handleSubmit}>
                <div className="container">
                    <label htmlFor="dropzone-file" className="label">
                        <div className="container2">
                            <svg
                                className="svg"
                                aria-hidden="true"
                                xmlns="http://www.w3.org/2000/svg"
                                fill="none"
                                viewBox="0 0 20 16"
                            >
                                <path
                                    stroke="currentColor"
                                    strokeLinecap="round"
                                    strokeLinejoin="round"
                                    strokeWidth="2"
                                    d="M13 13h3a3 3 0 0 0 0-6h-.025A5.56 5.56 0 0 0 16 6.5 5.5 5.5 0 0 0 5.207 5.021C5.137 5.017 5.071 5 5 5a4 4 0 0 0 0 8h2.167M10 15V6m0 0L8 8m2-2 2 2"
                                />
                            </svg>
                            <p className="text1">
                                <span className="font-semibold">
                                    Click para subir
                                </span>{" "}
                                o arrastra tu archivo aquí
                            </p>
                            <p className="text2">
                                Cualquier archivo en formato .xlsx
                            </p>
                        </div>
                        <input
                            id="dropzone-file"
                            type="file"
                            className="input2"
                            onChange={handleFileInputChange}
                        />
                    </label>
                </div>
                <button type="submit">Enviar</button>
            </form>
        </div>
    );
};

export default Upfile;
