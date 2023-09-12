import { PageWithNavbar } from "../../layouts/PageWIthNavbar"
import { usePositionListQuery } from "../../queries/usePositionListQuery"
import { ListRow } from "./ListRow"

export const PositionList = () => {
    const {data} = usePositionListQuery()
    return (
        <PageWithNavbar>
            <h1 className='text-3xl font-bold'>Positions</h1>
            <div className='mt-8  pl-5 pr-5 width-max'>
                {data?.map(position => (
                    <ListRow key={position.id} name={position.name} />
                ))}
            </div>
        </PageWithNavbar>
    )
}