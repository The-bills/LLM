import { useUploadCv } from "../queries/useUploadCv"

export const FileDrop = () => {
    const { mutateAsync, data, isLoading} = useUploadCv()

    const handleUpload = async (value?: Blob) => {
        if(!value) return
        let res = await mutateAsync({file: value})
        console.log(res)
    }


    return (
        <div className=''>
            {isLoading && <div>Loading...</div>}
                <input type="file" onChange={e => handleUpload(e.target.files?.[0])} />
        </div>
    )
}