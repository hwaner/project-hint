package kr.hwaner.spring.hint.board;

import static com.querydsl.core.types.PathMetadataFactory.*;

import com.querydsl.core.types.dsl.*;

import com.querydsl.core.types.PathMetadata;
import javax.annotation.processing.Generated;
import com.querydsl.core.types.Path;
import com.querydsl.core.types.dsl.PathInits;


/**
 * QBoard is a Querydsl query type for Board
 */
@Generated("com.querydsl.codegen.DefaultEntitySerializer")
public class QBoard extends EntityPathBase<Board> {

    private static final long serialVersionUID = 1421862970L;

    private static final PathInits INITS = PathInits.DIRECT2;

    public static final QBoard board = new QBoard("board");

    public final StringPath boardContent = createString("boardContent");

    public final NumberPath<Long> boardId = createNumber("boardId", Long.class);

    public final StringPath boardRegdate = createString("boardRegdate");

    public final StringPath boardTitle = createString("boardTitle");

    public final ListPath<kr.hwaner.spring.hint.comment.Comment, kr.hwaner.spring.hint.comment.QComment> commentList = this.<kr.hwaner.spring.hint.comment.Comment, kr.hwaner.spring.hint.comment.QComment>createList("commentList", kr.hwaner.spring.hint.comment.Comment.class, kr.hwaner.spring.hint.comment.QComment.class, PathInits.DIRECT2);

    public final kr.hwaner.spring.hint.user.QUser user;

    public final NumberPath<Integer> viewCnt = createNumber("viewCnt", Integer.class);

    public QBoard(String variable) {
        this(Board.class, forVariable(variable), INITS);
    }

    public QBoard(Path<? extends Board> path) {
        this(path.getType(), path.getMetadata(), PathInits.getFor(path.getMetadata(), INITS));
    }

    public QBoard(PathMetadata metadata) {
        this(metadata, PathInits.getFor(metadata, INITS));
    }

    public QBoard(PathMetadata metadata, PathInits inits) {
        this(Board.class, metadata, inits);
    }

    public QBoard(Class<? extends Board> type, PathMetadata metadata, PathInits inits) {
        super(type, metadata, inits);
        this.user = inits.isInitialized("user") ? new kr.hwaner.spring.hint.user.QUser(forProperty("user"), inits.get("user")) : null;
    }

}

