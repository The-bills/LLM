import { useNavigate } from "react-router"
import { useUploadCv } from "../queries/useUploadCv"
import { ImageIcon } from "../assets/icons"
import { useRef } from "react"

export const FileDrop = () => {
    const navigate = useNavigate()
    const inputRef = useRef<HTMLInputElement>(null)
    const { mutateAsync } = useUploadCv()

    const handleUpload = async (value?: Blob) => {
        if(!value) return
        console.log(value)
        let res = await mutateAsync({file: value})
        navigate(`/cv/${res?.id}`)
    }

    const handleDrop = (e: any) => {
        e.preventDefault()
        const file = e.dataTransfer.files?.[0]
        handleUpload(file)
    }

    return (
        <div
            onClick={() => inputRef.current?.click()}
            onDrop={handleDrop}
            onDragOver={e => e.preventDefault()}
            className='border-2 border-dashed max-w-2xl h-2xl flex flex-col items-center rounded-lg p-8 text-slate-600 cursor-pointer'
        >
            <div className="">
                <ImageIcon className='h-8 w-8' />
            </div>
            <div className='text-sm mt-3'>Upload a file or drag and drop</div>
            <div className="text-xs">PDF files up to 10MB</div>
            <input type="file" hidden ref={inputRef} onChange={e => handleUpload(e.target.files?.[0])} />
        </div>
    )
}