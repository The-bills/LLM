import { useMutation } from "react-query"

const BE_URL = 'http://127.0.0.1:5000'

export const useUploadCv = () => {

    const getBody = (file: Blob, name: string) => {
        const formData  = new FormData();
        formData.append('cv', file);
        formData.append('name', name);
        formData.append('category', 'developer');
        return formData
    }

    const mutation = useMutation<unknown, unknown, {file: Blob}>(({file}) => fetch(
        `${BE_URL}/cv`,
        {
            method: 'POST',
            body: getBody(file, 'unknown')
        }
    ).then(res => res.json()))

    return mutation
}