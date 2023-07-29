package db

import (
	"context"
	"go.mongodb.org/mongo-driver/mongo"

	"github.com/techyragu/goProject/endorlab/objects"
)

type mongodb struct {
	client *mongo.Client
}

func (mgo *mongodb) Store(ctx context.Context, object objects.Object) error {

	return nil
}

func (mgo *mongodb) GetObjectByID(ctx context.Context, id string) (objects.Object, error) {
	collection := 
	return nil
}

func (mgo *mongodb) GetObjectByName(ctx context.Context, name string) (objects.Object, error) {

	return nil
}

func (mgo *mongodb) ListObjects(ctx context.Context, kind string) ([]objects.Object, error) {

	return nil
}

func (mgo *mongodb) DeleteObject(ctx context.Context, id string) error  {

	return nil
}