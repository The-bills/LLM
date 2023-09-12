import { useCvListQuery } from "../../queries/useCvListQuery"
import { ListRow } from "./ListRow"

export const CvList = () => {
    const {data} = useCvListQuery()
    return (
        <div className=''>
            <h1 className='text-3xl font-bold'>All CVs</h1>
            <div className='mt-8  pl-5 pr-5 width-max'>
                {data?.map(cv => (
                    <ListRow key={cv.id} name={cv.name} category={cv.category} />
                ))}
            </div>
        </div>
    )
}