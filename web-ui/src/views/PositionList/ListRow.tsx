import { Link } from "react-router-dom"

type Props = {
    name: string
    id: string
}

export const ListRow = (p: Props) => {
    return (
        <div className='grid rows-2 border-b-2 pb-5 mt-5'>
            <div className='text-base font-semibold pb-1'>{p.name}</div>
            <div className='text-sm text-slate-700'>Sep 11, 2023</div>
            <Link to={`/position/${p.id}`} className='row-start-1 row-end-3 col-start-2 col-end-3 ml-auto mr-6 self-center border rounded pt-1 pr-2 pb-1 pl-2 text-sm font-semibold'>
                View details
            </Link>
        </div>
    )
}